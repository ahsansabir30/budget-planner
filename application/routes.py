from application import app, db
from flask import render_template, url_for, flash, redirect, request
from application.forms import PlanCreationForm, ExpenseForm
from application.models import Plan, Expenses

@app.route("/")
def plan_view():
    plans = Plan.query.all()
    return render_template('planner.html', plans=plans)

@app.route("/new-plan", methods=['GET', 'POST'])
def create_plan():
    header = "Create New Plan"
    form = PlanCreationForm()
    if form.validate_on_submit():
        new_plan = Plan(name=form.name.data, budget=form.budget.data)
        db.session.add(new_plan)
        db.session.commit()
        flash(f"Plan was created successfully {form.name.data}!", 'success')
        return redirect(url_for('plan_view'))

    return render_template('planform.html', form=form, header=header)

@app.route("/update-plan/<int:plan_id>", methods=['GET', 'POST'])
def update_plan(plan_id):
    # need to query database first
    plan = Plan.query.get_or_404(plan_id)
    form = PlanCreationForm()

    if form.validate_on_submit():
        plan.name = form.name.data
        plan.budget = form.budget.data
        db.session.commit()
        flash(f"Plan was updated successfully!", 'success')
        return redirect(url_for('plan_view'))
    elif request.method == 'GET':
        # loading form data
        form.name.data = plan.name
        form.budget.data = plan.budget

    header = f"Update Plan: {plan.name}"
    return render_template('planform.html', plan=plan, form=form, header=header)

@app.route("/delete-plan/<int:plan_id>/", methods=['GET', 'POST'])
def delete_plan(plan_id):
    plan = Plan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('plan_view'))

